# Head's UP

I am refurbhishsing an old markdown of mine, that gives you a brief walkthrough of how to set up and use a markdown syntax. You can find the original document at this [Github Repo](https://github.com/NevinKoshyDaniel/PrivateCollabsApp)

## Hosting Essentials

_PrivateCollabsApps(PCA)_ is an **Open Source Self Deployment Workspace Solution** built on top of popular Open Source Technologies,aiming to integrate various functionalities.
The pandemic has opened up the need for large scale collaboration apps, and large organizations, especially in the business and education sectors are trying to incorporate their entities under a single umbrella.<br>
The ever-growing privacy concerns are the reason for the use of open-source software stacks, and the capability to manage your formal communications in a private stack, highly customisable stack instance would be highly appreciated by the privacy-centric instances. So let's try to host a student version of Microsoft Azure.

### Steps to Replicate the Solution

 - Active MicroSoft Azure Account 
 - Create 2 VMs, A Storage Account, A DNS Zones, A Virtual Network, A KeyVault inside a resource group. <br> If you are useing docker images, you will be required o make use of Azure Kubernetes Services under the same resouce group. Active Directory Integrations follows suit. 
 - The VM hosting Jitsi Meet should have 1 GB RAM and 1 vCPU atleast. At the very least, opt for B1s VMs. <br> This setup will run smoothly for 10+ participants simultaneously sharing their videos in HD. It is advised to increase the RAM and CPU capabilities if you are having a lot of simulataneous conferences.  It is advised that the VM reserves a static IP, as it can come in handy at times. <br>The individual hosting help can be found at [Jitsi Meet Hosting](https://github.com/NevinKoshyDaniel/PrivateCollabsApp/tree/main/Jitsi%20Meet)
 - The VM hosting Rocket.Chat should have 2 GB RAM and 1 vCPU atleast. At the very least, opt for B1ms VMs. <br> This setup will run smoothly for 50+ active participants simultaneously communicating.  It is advised to increase the RAM and CPU capabilities if you are having more simultaneous users. It is advised that the VM reserves a static IP. <br>The individual hosting help can be found at [Rocket.Chat Hosting](https://github.com/NevinKoshyDaniel/PrivateCollabsApp/tree/main/Rocket.Chat)
 - Both the VMs will require SSL certificates, and ensure they are atleast Self Signed. <br> There will be access issues if the certificates are not signed.
 - Connect to the Rocket.Chat public IP, login and configure the necessary Admin settings and kindly register the server for use.
 - Ensure the Specific ports and protocols are enabled in the Network Security Groups. [_Let's Encrypt_](https://letsencrypt.org/) would be sufficient. <br>Incorrect configurations would lead to no traffic, as the applications listen on specific ports, and no traffic flow rule to them will cause failures. 
 - Ensure the Virtual Network encompossess the properly confiured Network Security Groups.
 - The DNS Zone comes into play if you are intenting to use a custom domain. 
 - KeyVault can be handy to store neccessary SSH credentials, and other admin specific data, especially if container instances are used.
 - Azure Blob Sotrage can be made use of to provide a cloud based storage solution.
 - Azure Active Directory Services can be made use of for enterprise identity service, with single sign-on, multifactor authentication, and conditional access needs. 

### Possible Issues and Heads-ups!
  
 - Issues may arise with the SSL certificates, and both the VMs should have atleast self signed certificates
 - Becareful with the DNS configurations, and ensure that the mapping is correct
 - Hosting the services with Azure Kubernetes Services may causes issues at times; 
 - Configurations of the Key Vault and essential data storages should be ensured.
 - Configurating Rocket.Chat with Azure Blob Storage as the cloud storage needs a bit of tinkering
 - Ensure the connection to the jitsi meet instance launcher is having a valid address
 - At times, the connection issues may be due to incorrectly configured proxies/ network security rules. Ensure the correct port access are granted.

<br> You can try out my version at : [Application URL](https://rocketchatvm.southindia.cloudapp.azure.com/home) <br>
