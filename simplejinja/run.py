#Imports from Jinja2
from jinja2 import Environment, FileSystemLoader
import csv

file_loader = FileSystemLoader('templates')

env = Environment(loader=file_loader)

template = env.get_template('cisco_template.j2')

with open ("ip_info.csv") as f:
    csv_data=csv.reader(f)
    for row in csv_data:
        csv_router_name = row[0]
        csv_G001_ip = row[1]
        csv_ntp_server_ip = row[2]

        #render unique data over template
        output = template.render(router_name=csv_router_name,
                                    G001_ip = csv_G001_ip,
                                    ntp_server_ip = csv_ntp_server_ip
        )
        with open(csv_router_name + ".txt","w") as txtf:
            txtf.write(output)
