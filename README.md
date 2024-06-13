# Terraform AWS EC2 Instance with Specific Private IP

This Terraform configuration sets up an AWS environment including a VPC, a subnet, and an EC2 instance with a specified private IP address within the subnet.

## Prerequisites

- [Terraform](https://www.terraform.io/downloads.html) installed.
- AWS account with credentials configured locally (`aws configure`).

## Configuration Details

1. **VPC and Subnet**: A Virtual Private Cloud (VPC) and a subnet are created. The subnet is defined within the VPC with the CIDR block `10.0.1.0/24`.
2. **Security Group**: A security group is created to allow inbound SSH access (port 22) from any IP address (`0.0.0.0/0`) and all outbound traffic.
3. **Network Interface**: A network interface is created in the specified subnet with the desired private IP address (`10.0.1.10`).
4. **EC2 Instance**: An EC2 instance is launched and the previously created network interface is attached to it.

## Files

- `main.tf`: Contains the main Terraform configuration.

## Usage

### Step 1: Initialize Terraform

First, initialize the Terraform working directory, which will download the required provider and set up the environment.

```sh
terraform init
