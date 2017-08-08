#!/bin/bash
clear
echo "About to uninstall... Hold on!"
git checkout master
git pull
echo "#!/bin/bash" > ../adinstall.sh
echo "cd untangled-2017" >> ../adinstall.sh
echo "clear" >> ../adinstall.sh
echo "echo 'About to update... Hold on!'" >> ../adinstall.sh
echo "git checkout Admin" >> ../adinstall.sh
echo "git pull" >> ../adinstall.sh
echo "cp player_example player_save" >> ../adinstall.sh
echo "sh adinstall.sh" >> ../adinstall.sh
clear
echo "Sad to see you go."
echo "Just run the following to come back:"
echo "sh ../adinstall.sh"