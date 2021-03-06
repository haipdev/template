# haip.template

[![License](https://img.shields.io/github/license/haipdev/template.svg)](LICENSE)
[![Build Status](https://travis-ci.org/haipdev/template.svg?branch=master)](https://travis-ci.org/haipdev/template)

haip.template is Jinja2 based async template rendering module.

## Features

* **minimalistic**: a single exported async function "render"
* **autoreturn-type**: the return data type is derived from the file suffix

## Getting Started

### Installing

```sh
pip install haip-template
```

or from source:

```sh
git clone https://github.com/haipdev/template.git
```

### Usage

> async def render(template_filename, *, template_dir=None, **args)

The template-file is defined by *config.template_dir/template_dir/template_filename*. **args are used to fillin the placeholders in the template_file and the suffix of the template_file determines the return type. E.g. "template_name.json" will return a json structure (dict). *render* will propagate exceptions as they are raised by the underlaying modules.

Suffix handling is as follows:

* .json : json struct (dict)
* .sql : string (but **args values will be escaped)
* .* : string

> Notice: in sql templates only the arguments are escaped not the query itself. So use placeholders (jinja2 {{ }}) in your query and provide values per arguments.

### Example

#### config (using haip.config)

```yaml
template-dir: /path-to-template-dir/
```

mytemplate.jinja2

```jinja2
Hello my name is {{ firstname }} {{ lastname }}!
```

#### python implementation

```python
import haip.config as config
import haip.template as template

config.load('/path-to-my-config-dir')
document = await template.render('mytemplate.jinja2', firstname='Reinhard', lastname='Hainz')
```

If mytemplate.jinja is in a subdirectory of the template-dir (e.g. /path-to-template-dir/mysubdir/):

```python
document = await template.render('mytemplate.jinja2', template_dir='mysubdir', firstname='Reinhard', lastname='Hainz')
```

You can also use absolute paths in the template_dir argument of the render function.

## Running the tests

Tests are written using pytest and located in the "tests" directory.

```sh
pytest tests
```

## Contributing

Feel free to use and enhance this project. Pull requests are welcome.

## Authors

* **Reinhard Hainz** - *Initial work* - [haipdev](https://github.com/haipdev)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Dependencies

* [haip_config](https://github.com/haipdev/config)
* [jinja2](http://jinja.pocoo.org/)
