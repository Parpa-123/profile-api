Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.box_version = "~> 20210929.0.0"
  config.vm.boot_timeout = 600

  # Change forwarded port to 5173
  config.vm.network "forwarded_port", guest: 5173, host: 5173

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y python3-venv zip
    touch /home/vagrant/.bash_aliases
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
      echo "alias python='python3'" >> /home/vagrant/.bash_aliases
    fi
  SHELL

  config.vm.provider "virtualbox" do |vb|
    vb.gui = true
  end
end