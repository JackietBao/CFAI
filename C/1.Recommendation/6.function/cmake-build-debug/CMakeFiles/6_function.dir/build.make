# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.19

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "D:\SoftWare\JetBrains\CLion 2021.1.3\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "D:\SoftWare\JetBrains\CLion 2021.1.3\bin\cmake\win\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = D:\Github\CFAI\C\1.Recommendation\6.function

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = D:\Github\CFAI\C\1.Recommendation\6.function\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/6_function.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/6_function.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/6_function.dir/flags.make

CMakeFiles/6_function.dir/main.c.obj: CMakeFiles/6_function.dir/flags.make
CMakeFiles/6_function.dir/main.c.obj: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Github\CFAI\C\1.Recommendation\6.function\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/6_function.dir/main.c.obj"
	D:\Lang\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\6_function.dir\main.c.obj -c D:\Github\CFAI\C\1.Recommendation\6.function\main.c

CMakeFiles/6_function.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/6_function.dir/main.c.i"
	D:\Lang\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E D:\Github\CFAI\C\1.Recommendation\6.function\main.c > CMakeFiles\6_function.dir\main.c.i

CMakeFiles/6_function.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/6_function.dir/main.c.s"
	D:\Lang\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S D:\Github\CFAI\C\1.Recommendation\6.function\main.c -o CMakeFiles\6_function.dir\main.c.s

CMakeFiles/6_function.dir/func.c.obj: CMakeFiles/6_function.dir/flags.make
CMakeFiles/6_function.dir/func.c.obj: ../func.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Github\CFAI\C\1.Recommendation\6.function\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/6_function.dir/func.c.obj"
	D:\Lang\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles\6_function.dir\func.c.obj -c D:\Github\CFAI\C\1.Recommendation\6.function\func.c

CMakeFiles/6_function.dir/func.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/6_function.dir/func.c.i"
	D:\Lang\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E D:\Github\CFAI\C\1.Recommendation\6.function\func.c > CMakeFiles\6_function.dir\func.c.i

CMakeFiles/6_function.dir/func.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/6_function.dir/func.c.s"
	D:\Lang\mingw64\bin\gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S D:\Github\CFAI\C\1.Recommendation\6.function\func.c -o CMakeFiles\6_function.dir\func.c.s

# Object files for target 6_function
6_function_OBJECTS = \
"CMakeFiles/6_function.dir/main.c.obj" \
"CMakeFiles/6_function.dir/func.c.obj"

# External object files for target 6_function
6_function_EXTERNAL_OBJECTS =

6_function.exe: CMakeFiles/6_function.dir/main.c.obj
6_function.exe: CMakeFiles/6_function.dir/func.c.obj
6_function.exe: CMakeFiles/6_function.dir/build.make
6_function.exe: CMakeFiles/6_function.dir/linklibs.rsp
6_function.exe: CMakeFiles/6_function.dir/objects1.rsp
6_function.exe: CMakeFiles/6_function.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=D:\Github\CFAI\C\1.Recommendation\6.function\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking C executable 6_function.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\6_function.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/6_function.dir/build: 6_function.exe

.PHONY : CMakeFiles/6_function.dir/build

CMakeFiles/6_function.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\6_function.dir\cmake_clean.cmake
.PHONY : CMakeFiles/6_function.dir/clean

CMakeFiles/6_function.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" D:\Github\CFAI\C\1.Recommendation\6.function D:\Github\CFAI\C\1.Recommendation\6.function D:\Github\CFAI\C\1.Recommendation\6.function\cmake-build-debug D:\Github\CFAI\C\1.Recommendation\6.function\cmake-build-debug D:\Github\CFAI\C\1.Recommendation\6.function\cmake-build-debug\CMakeFiles\6_function.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/6_function.dir/depend

