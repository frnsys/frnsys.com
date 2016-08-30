# personal site (frnsys.com)

- `projects.yaml` is used to build the index page
- `projects/*.md` describe project-specific pages

to build the site, run `python build.py`. this requires `pyyaml`, `jinja`, and `nom` and should use `python3`.

the site is built to `.build`.

you can run a little server in there to develop the site locally or you can sync it to a remote server, e.g.:

    rsync -ravu .build/ me@server.foo:/srv/frnsys/