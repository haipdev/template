import os
import json
import jinja2
import haip.config as config

async def render(template_filename, *, template_dir=None, **args):
    cfg = config.get(template_dir=config.MANDATORY)
    if template_dir is None:
        template_dir = cfg.template_dir
    elif not template_dir.startswith('/'):
        template_dir = cfg.template_dir + os.sep + template_dir
    j2 = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), enable_async=True)
    tpl = j2.get_template(template_filename)
    resp = await tpl.render_async(**args)
    return _decode(resp, template_filename)

def _decode(data_string, filename):
    _, suffix = os.path.splitext(filename)
    if suffix == '.json':
        return json.loads(data_string)
    return data_string
    