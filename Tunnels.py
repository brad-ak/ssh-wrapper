## Tunnel class to track and create tunnels


class Tunnel(object):
    tunnel_instances = {}
    tunnel_count = 0

    def __init__(self, tunnel_type, cmd_line):
        self.tunnel_type = tunnel_type
        self.cmd_line = cmd_line
        Tunnel.tunnel_count += 1
        self.tunnel_id = Tunnel.tunnel_count

        def return_info(self):
            print(str(self.tunnel_id) + " " + str(self.tunnel_type) + " " + str(self.cmd_line))

        def add_to_dict(self):
            Tunnel.tunnel_instances[self.tunnel_id] = self

        @classmethod
        def return_all_tunnels(cls):
            print("Hello")
            print(list(Tunnel.tunnel_instances.values().tunnel_id))
