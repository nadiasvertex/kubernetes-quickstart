# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/xenial64"
  N = 6
  D = 3
  (1..N).each do |machine_id|
     config.vm.define "machine#{machine_id}" do |machine|
        machine.vm.hostname = "machine#{machine_id}"
        machine.vm.network "private_network", ip: "192.168.77.#{1+machine_id}", netmask: 24
        config.vm.provider "virtualbox" do |v|
         v.memory = 1026
        end 
        (0..D-1).each do |d|
          machine.vm.provider :virtualbox do |vb|
              unless File.exist?("disk-#{machine_id}-#{d}.vdi")
                  vb.customize [ "createmedium", "--filename", "disk-#{machine_id}-#{d}.vdi", "--size", 1024*1024 ]
              end
              vb.customize [ "storageattach", :id, "--storagectl", "SCSI", "--port", 2+d, "--device", 0, "--type", "hdd", "--medium", "disk-#{machine_id}-#{d}.vdi" ]
          end      
        end
        # Only execute the Ansible provisioner,
        # when all the machines are up and ready.
        if machine_id == N
           machine.vm.provision :ansible do |ansible|
              # Disable default limit to connect to all the machines
              ansible.limit = "all"
              ansible.playbook = "provisioning/playbook.yaml"
              ansible.groups = {
                "load_balancer" => ["machine1"],
                "orchestrated"  => ["machine2", "machine3", "machine4", "machine5", "machine6"]
              }
           end
        end
     end
  end
end
