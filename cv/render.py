# %%
from jinja2 import Environment, FileSystemLoader, select_autoescape
import yaml

# Opzetten Jinja2 omgeving met instellingen
env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml']),
    trim_blocks=True,
    lstrip_blocks=True,
)

# Lezen data
with open('data.yaml') as f:
    data = yaml.safe_load(f)
    # print(data)


# %%
# Render
template = env.get_template('cv.html')
output = template.render(data=data)

# Save
with open('public/cv.html', 'w') as f:
    f.write(output)
