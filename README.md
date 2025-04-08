# ProtonLaunchHelperScript
A python3 script to help in using steam proton to launch exes

So... it *might* work out of the box but ideally you'd read and edit this script before you use it!
In particular check the paths, proton_builds_folder should point to a directory with at least one folder containing proton in it (if you've used steam proton to run a steam game then you'll have proton installed in steamapps).

To install, you can place it in ~/.local/bin and make it executable then just run it from the directory where the .exe is and follow the promots.
Failing that, place it in the same directory as your .exe and run it there but that's a bit messy.

The basic flow is:
1) select a .exe to run
2) select a proton version to use
3) select a compat data folder
4) send it!
