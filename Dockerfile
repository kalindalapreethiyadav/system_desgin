# Use lightweight base image
FROM ubuntu:22.04

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install basic dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    software-properties-common \
    ca-certificates \
    gnupg \
    lsb-release \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# ----------------------------
# Install Ansible
# ----------------------------
RUN pip3 install --no-cache-dir ansible

# ----------------------------
# Install Terraform
# ----------------------------
RUN wget https://releases.hashicorp.com/terraform/1.7.5/terraform_1.7.5_linux_amd64.zip && \
    unzip terraform_1.7.5_linux_amd64.zip && \
    mv terraform /usr/local/bin/ && \
    rm terraform_1.7.5_linux_amd64.zip

# ----------------------------
# Install Docker CLI
# ----------------------------
RUN apt-get update && apt-get install -y docker.io && \
    rm -rf /var/lib/apt/lists/*

# ----------------------------
# Verify installations
# ----------------------------
RUN python3 --version && \
    pip3 --version && \
    ansible --version && \
    terraform -version && \
    docker --version

# Set working directory
WORKDIR /workspace

CMD ["/bin/bash"]