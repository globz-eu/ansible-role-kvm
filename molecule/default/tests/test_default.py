import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_dependencies(host):
    packages = [
        'libvirt-bin',
        'qemu-kvm',
        'bridge-utils',
        'virt-manager',
        'virtinst',
        'ovmf'
    ]

    for package in packages:
        tested_package = host.package(package)

        assert tested_package.is_installed


def test_user_in_libvirt_group(host):
    vagrant_user = host.user('root')

    assert 'libvirt' in vagrant_user.groups
    assert 'kvm' in vagrant_user.groups
