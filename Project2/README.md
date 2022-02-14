# Part 1 - Build a VPC

1. Create a VPC
    - Specify a /24 private IP address range
      - 10.0.0.0/24
  ![VPC]("https://user-images.githubusercontent.com/70331126/153887650-054f1fc1-4924-422d-b839-e69a899c0905.png")


2. Create a subnet
    - Specify a /28 private IP address range
    - Attach it to your VPC
        - 10.0.0.0/28
 ![Subnet](Subnet.png)

3. Create an internet gateway
    - Attach it to your VPC
![Gateway](Gateway.png)


4. Create a route table
    - Attach it to your VPC
    - Associate it with your subnet
    - Add a routing table rule that sends traffic to all destinations to your internet gateway
 ![Route Table](Route.png)


5. Create a security group
    - Allow SSH for a set of trusted networks including:
      - Your home / where you usually connect to your instances from
      - Wright State (addresses starting with 130.108)
      - Instances within the VPC
![Security Group](SecurityGroup.png)
- Inbound Rules Above

# Part 2 
- EC2 instances
1. Create a new instance. 
    - AMI selected
    - Instance type selected
   
 I clicked on lanuch instances on the EC2 Dashboard. I chose Ubuntu Server 20.04 LTS (HVM), and then choose t2.micro on the next page.

2. Attach the instance to your VPC. As discussed there are different pathways to doing this. Say how you did it.

    To attach the instance to the VPC, the  next page shows network details. Under the network I attached the PETERANGELO-VPC to the instance.
    This caused the subnet to be attached to the instance now.
    
![Instance Created](Instance.png)

3. Determine whether a Public IPv4 address will be auto-assigned to the instance. Justify your choice to do so (or not do so)

   The subnet diables an auto IP address to be assinged. We have to use a Elastic IP which enables us to remmap the address to other instances in the VPC. 
   
4. Attach a volume to your instance. As discussed there are different pathways to doing this. Say how you did it.

    Within the next step of creating the instance I had to select a volume to add. I decided to stay at the deafult which was SSD (gp2).

5. Tag your instance with a "Name" of "YOURLASTNAME-instance". Say how you did it.

    The next step was adding a tag. I went to add tags and  added Peterangelo-instance.

6. Associate your security group, "YOURLASTNAME-sg" to your instance. Say how you did it.

    In the instance i clicked "actions" and then chose "secuirty",  "add security groups" and choose the ones I created called PETERANGELO-sg.

7. Reserve an Elastic IP address. Tag it with "YOURLASTNAME-EIP". Associate the Elastic IP with your instance. Say how you did it.

   Under Network Settings on the side of the page clicked on Elastic IP. Then clicked on Allocate Elastic IP address and added
    a tag to this IP called Peterangelo-EPI. Then I clicked on Action then Assoacite Elastic IP and associated the this IP to the instance we created. 

8. Create a screenshot your instance details and add it to your project write up.
![Instance With Details](Instance2.png)


9. ssh in to your instance. Change the hostname to "YOURLASTNAME-AMI" where AMI is some version of the AMI you chose. Say how you did it.
    Used the command ssh -i ceg3120 ubuntu@44.196.7.108
    Change host name by typing sudo hostnamectl set-hostname Peterangelo-UbuntuAMI

  
10. Create a screenshot your ssh connection to your instance and add it to your project write up - make sure it shows your new hostname.
![Connecting to Instance](connect.png)

Note: You may delete all created resources once done to save monies. No really, trash it - especially the instance and disassociate and release the elastic ip

