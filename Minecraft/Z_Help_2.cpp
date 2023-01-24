///////////////////////////////////////////////////////////////////////////
// IMPORTS
///////////////////////////////////////////////////////////////////////////

#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include <string>
#include <iostream>

using namespace std;
void processInput(GLFWwindow *window);


///////////////////////////////////////////////////////////////////////////
// WINDOW
///////////////////////////////////////////////////////////////////////////

// SETTINGS
const unsigned int WIDTH = 800;
const unsigned int HEIGHT = 600;
const char* TITEL = "Minecraft";
const float bg_color[3] = {0.5f, 0.3f, 0.7f};

int createWindow() {
    glfwInit();

    //more Hints for Settings
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    // Create Window
    GLFWwindow* window = glfwCreateWindow(WIDTH, HEIGHT, TITEL, NULL, NULL);
    if (window == NULL)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
    {
        std::cout << "Failed to initialize GLAD" << std::endl;
        return -1;
    }

    glViewport(0, 0, WIDTH, HEIGHT);

    while (!glfwWindowShouldClose(window))
    {
        glClearColor(bg_color[0], bg_color[1], bg_color[2], 0.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        // draw

        glfwSwapBuffers(window);
        glfwPollEvents();
    }
    glfwTerminate();
    return 0;
}
createWindow();
///////////////////////////////////////////////////////////////////////////
// INPUT
///////////////////////////////////////////////////////////////////////////
/*
glfwSerKeyCallback(window, key_callback);  // bevore glViewport()
void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods)
{
    if (key == GLFW_KEY_E && action == GLFW_PRESS) // before glViewport
        activate_airship();
}
*/
///////////////////////////////////////////////////////////////////////////
// DRAW
///////////////////////////////////////////////////////////////////////////
