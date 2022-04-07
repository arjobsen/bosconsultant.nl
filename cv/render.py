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
# Render front_page.html
# template = env.get_template('front_page.html')
# output = template.render(data=data)

# # Save
# with open('public/front_page.html', 'w') as f:
#     f.write(output)


# %%
# Render track_record.html
template = env.get_template('track_record.html')
output = template.render(data=data)

# Save
with open('public/track_record.html', 'w') as f:
    f.write(output)
