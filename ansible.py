#!/usr/bin/python
from collections import namedtuple
import  sys
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager  import   VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.executor.playbook_executor import PlaybookExecutor
def InventoryManagerStudy():
       dl=DataLoader()
       im=InventoryManager(loader=dl,sources=["/etc/ansible/hosts"])
       vm=VariableManager(loader=dl,inventory=im)
       Options = namedtuple("Options",[
        "connection", "remote_user", "ask_sudo_pass", "verbosity", "ack_pass",
        "module_path", "forks", "become", "become_method", "become_user", "check",
        "listhosts", "listtasks", "listtags", "syntax", "sudo_user", "sudo", "diff"
       ])
       options=Options(connection='smart', remote_user=None, ack_pass=None, sudo_user=None, forks=5, sudo=None, ask_sudo_pass=       False, verbosity=5, module_path=None, become=None, become_method=None, become_user=None, check=False, diff=False,
       listhosts=None, listtasks=None, listtags=None, syntax=None)
       play_source = dict(name="ansible play",
           hosts="web",
           gather_facts="yes",
           tasks=[
               dict(action=dict(module="shell",args="ls /"))
           ]
       )
       play=Play().load(play_source,variable_manager=vm,loader=dl)
       passwords = dict()  
    
       tqm = TaskQueueManager(
          inventory=im,
          variable_manager=vm,
          loader=dl,
          options=options,
          passwords=passwords,
        )
       result = tqm.run(play)
       print(result)


if __name__=='__main__':
        InventoryManagerStudy()
   
