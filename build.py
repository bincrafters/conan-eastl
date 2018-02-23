#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bincrafters import build_template_default

if __name__ == "__main__":

    builder = build_template_default.get_builder()
    
    builder.builds = filter(lambda build: build.options['eastl:shared'] == False , builder.items)

    builder.run()
