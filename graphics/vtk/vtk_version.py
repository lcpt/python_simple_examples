#!/usr/bin/env python3

from vtk.vtkCommonCore import vtkVersion


def vtk_version_ok(major, minor, build):
    """
    Check the VTK version.

    :param major: Major version.
    :param minor: Minor version.
    :param build: Build version.
    :return: True if the requested VTK version is greater or equal to the actual VTK version.
    """
    needed_version = 10000000000 * int(major) \
                     + 100000000 * int(minor) \
                     + int(build)
    ver= vtkVersion()
    vtk_major= ver.GetVTKMajorVersion()
    vtk_minor= ver.GetVTKMinorVersion()
    vtk_build= ver.GetVTKBuildVersion()
    
    if(vtk_major>=9):
        from vtk.vtkCommonCore import VTK_VERSION_NUMBER
        vtk_version_number= VTK_VERSION_NUMBER
    else:
        # Expand component-wise comparisons for VTK versions < 8.90.
        vtk_version_number = 10000000000 * vtk_major \
                             + 100000000 * vtk_minor \
                             + vtk_build
    if vtk_version_number >= needed_version:
        return True
    else:
        return False


def main():
    print('VTK Version:',vtkVersion.GetVTKVersion())
    if not vtk_version_ok(9, 0, 0):
        print('You need VTK version 9.0.0 or greater to run this program.')
        return

    test_versions = ((9, 2, 20220831), (9, 19, 0))
    for ver in test_versions:
        if vtk_version_ok(*ver):
            print('This code works for VTK Versions >=', '.'.join(map(str, ver)))
        else:
            print('You need VTK Version', '.'.join(map(str, ver)), 'or greater.')
    print()


if __name__ == '__main__':
    main()
