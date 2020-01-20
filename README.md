# Vagrant

Install KVM QEMU and virt-manager on Ubuntu Bionic.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see defaults/main.yml):

```yaml
kvm_user: "root"
```

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  become: true
  vars:
    kvm_user: "user"
  roles:
    - role: kvm
```

## License

MIT
