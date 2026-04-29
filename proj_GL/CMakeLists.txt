cmake_minimum_required(VERSION 4.2)
project(proj_Gl)

set(CMAKE_CXX_STANDARD 20)

add_subdirectory(external)


find_package(OpenGL REQUIRED)

set(libs
        ${OPENGL_LIBRARY}
        glfw
        glad
        glm
)

add_executable(${PROJECT_NAME} src/main.cpp)
target_link_libraries(${PROJECT_NAME} ${libs})