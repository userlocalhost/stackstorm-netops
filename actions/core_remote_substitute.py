from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

from st2common.runners.base_action import Action


class CoreRemoteSubstitute(Action):
    def connect(self, host, device_type, username, password):
        try:
            net_connect = ConnectHandler(
                device_type=device_type,
                host=host,
                username=username,
                password=password,
            )
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as e:
            raise RuntimeError(e)

        return net_connect

    def run(self, host, cmd, device_type, username, password):
        net_connect = self.connect(host, device_type, username, password)

        output = net_connect.send_command(cmd)

        return (True, output)
