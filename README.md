# 🐳 Docker Project Template - Coding United Club

### Welcome to the official Docker project template for the **Coding United Club**! I am John Swindell, a fellow Club member, and will be walking you through this template guide! 

## Table of Contents

* [Overview](#overview)
* [What is Docker?](#what-is-docker)
* [Prerequisites](#prerequisites)
* [Key Files in This Template](#key-files-in-this-template)
* [Step 1: Get the Template](#step-1-get-the-template)
* [Step 2: Explore the Sample Application](#step-2-explore-the-sample-application)
* [Step 3: Build the Docker Image](#step-3-build-the-docker-image)
* [Step 4: Run the Docker Container](#step-4-run-the-docker-container)
* [Step 5: Accessing the Application](#step-5-accessing-the-application)
* [Customizing for Your Own Project](#customizing-for-your-own-project)
* [Common Docker Commands](#common-docker-commands)
* [Getting Help](#getting-help)
* [License](#license)

---

Before we get started, the goal of this template provides a starting point for containerizing applications, especially Python applications, specifically using Docker.

Don't worry, I know it's scary, but I've got your back and I'll walk you through it.

Let's go!

---

## Overview

This template helps you:
* Understand the basics of Docker and `Dockerfile` structure.
* Containerize a simple Python web application.
* Learn how to build Docker images and run containers.
* Provide a consistent environment for your applications.
* Last, but certainly not least, will prepare you to work with us on our upcoming club website project!

---

## What is Docker?

Docker is a platform that uses OS-level virtualization to deliver software in packages called **containers**. Containers are isolated from one another and bundle their own software, libraries, and configuration files; they can communicate with each other through well-defined channels. This makes it easy to create, deploy, and run applications in different environments consistently.

**Some cool benefits:**
* **Consistency:** The classic: "Well, it works on my computer" is no longer an issue!
* **Portability:** Run your container anywhere Docker is installed.
* **Isolation:** Dependencies for one app don't conflict with others.
* **Scalability:** Easier to scale applications.

---

## Prerequisites

Before you begin, ensure you have the following installed:

1.  **Docker Desktop (or Docker Engine on Linux):** Download from [docker.com](https://www.docker.com/products/docker-desktop/).
2.  **Git:** Download from [git-scm.com](https://git-scm.com/downloads) (if you plan to clone).
3.  A **Terminal / Command Prompt** for running Docker commands.

---

## The Important Files in This Template

* **`Dockerfile`**: This is the blueprint for building your Docker image. It contains a set of instructions Docker uses to assemble the image.
* **`.dockerignore`**: Similar to `.gitignore`, this file lists files and directories that should be excluded when building the Docker image (i.e., not copied into the image).
* **`app/` directory**: Contains the sample Python application to be containerized.
    * `app/app.py`: A very simple Python HTTP server.
    * `app/requirements.txt`: (Optional) For listing Python dependencies. Our current sample `app.py` has no external dependencies.
* **`README.md`**: This file!

---

## Step 1: Get the Template

1.  **Clone this repository:**
    ```bash
    git clone [https://github.com/codindUnited/docker-template.git](https://github.com/codingUnited/docker-template.git) your-docker-project
    cd your-docker-project
    ```
    (Of course, make sure to replace `codingUnited` with the actual GitHub organization name you're using, and `your-docker-project` with your desired folder name).

---

## Step 2: Explore the Sample Application

The `app/app.py` file contains a very basic Python HTTP server. It's designed to run inside the Docker container and serve a simple HTML page. It uses environment variables defined in the `Dockerfile` (`APP_NAME`, `GREETING_MESSAGE`) and listens on port 8000.

---

## Step 3: Build the Docker Image

The `docker build` command builds an image from a `Dockerfile`.

1.  Navigate to the root directory of this template (where the `Dockerfile` is).
2.  Run the following command:
    ```bash
    docker build -t coding-united-app .
    ```
    * `-t coding-united-app`: This tags (names) your image `coding-united-app`. You can choose any name:tag combination.
    * `.`: This specifies that the build context (the set of files to send to the Docker daemon) is the current directory.

    You should see Docker stepping through the instructions in your `Dockerfile`.

---

## Step 4: Run the Docker Container

Once the image is built, you can run it as a container using `docker run`.

```bash
docker run -d -p 8080:8000 --name my-python-app coding-united-app
* `docker run`: The command to run a container.
* `-d`: Runs the container in "detached" mode (in the background).
* `-p 8080:8000`: This **publishes** a port. It maps port `8080` on your host machine to port `8000` inside the container (where our Python app is listening, as defined by `EXPOSE 8000` in the Dockerfile and the `app.py` script). You can change the host port (e.g., `-p 3000:8000`).
* `--name my-python-app`: Gives your running container a memorable name.
* `coding-united-app`: The name of the image you want to run.
```
---

## Step 5: Accessing the Application

Open your web browser and go to:
[http://localhost:8080](http://localhost:8080)

You should see the greeting message from the Python application running inside the Docker container! If you used a different host port in the `docker run` command (e.g., `-p 3000:8000`), then access it via `http://localhost:3000`.

---

## Customizing for Your Own Project

To use this template for your own Python (or other type) application:

1.  **Replace `app/` contents:**
    * Delete the sample `app/app.py` and `app/requirements.txt`.
    * Place your own application files into the `app/` directory. For example, if you have a Flask or Django project, its main files would go here.

2.  **Update `Dockerfile`:**
    * **Base Image:** If your application isn't Python, or requires a specific Python version, change the `FROM` instruction (e.g., `FROM node:18-slim` for a Node.js app).
    * **Dependencies:**
        * If your Python app needs packages, list them in `app/requirements.txt`. Then, ensure these lines are uncommented and correct in your `Dockerfile`:
            ```dockerfile
            COPY ./app/requirements.txt /app/requirements.txt
            RUN pip install --no-cache-dir -r requirements.txt
            ```
        * For other languages, use their respective package managers (e.g., `npm install` for Node.js, `bundle install` for Ruby).
    * **`EXPOSE` Port:** Change the `EXPOSE` instruction if your application inside the container listens on a port other than `8000`.
    * **`CMD` Instruction:** Modify the `CMD` instruction to correctly start your specific application. For example, for a Flask app typically run with `flask run --host=0.0.0.0 --port=5000`, your `CMD` might be `CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]`. Ensure the port in the `CMD` matches your `EXPOSE` port.

3.  **Rebuild your image** (`docker build -t your-new-app-name .`) and **run the new container** (`docker run -p <host_port>:<container_port> your-new-app-name`).

---

## Common Docker Commands

Here's a quick reference for some frequently used Docker commands:

* **List Images:**
    ```bash
    docker images
    ```
* **List Running Containers:**
    ```bash
    docker ps
    ```
* **List All Containers (running or stopped):**
    ```bash
    docker ps -a
    ```
* **Stop a Running Container:**
    ```bash
    docker stop <container_name_or_id>
    ```
    (e.g., `docker stop my-python-app`)
* **Remove a Stopped Container:**
    ```bash
    docker rm <container_name_or_id>
    ```
* **Remove an Image:**
    * First, make sure no containers are using the image (stop and remove them).
    ```bash
    docker rmi <image_name_or_id>
    ```
* **View Logs of a Container:**
    ```bash
    docker logs <container_name_or_id>
    ```
    (For detached containers, this is how you see their output.)
* **Execute a Command in a Running Container (e.g., get a shell):**
    ```bash
    docker exec -it <container_name_or_id> bash
    ```
    (This gives you an interactive terminal session inside the container, if `bash` is available in the image. For minimal images like `alpine`, use `sh`.)

---

## Getting Help

If you have questions, run into issues, or want to learn more:
* Ask your fellow Coding United Club members!
* Refer to the official Docker documentation: [Docker Docs](https://docs.docker.com/)
* Explore Docker Hub for pre-built images: [Docker Hub](https://hub.docker.com/)
* Feel free to @ me or ask in our: [Discord](https://discord.gg/n8xYkS46MG)
* Find more information on our: [Club Site](https://coding-united-commons.pages.dev/)

---

### Thank you for reading the template guide, and I hope you found it helpful :)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
