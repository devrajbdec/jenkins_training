# jenkins_training

This requires a node be defined as pyproject. To do this go to manage jenkins, select nodes and then add the label pyproject
It requires the folder /home/ubuntu/devraj_jenkins and /home/ubuntu/devraj_jenkins/build to be available 
add the jenkins to sudoers without password using **visudo** 
and add the line towards the end
jenkins ALL=(ALL) NOPASSWD: ALL
