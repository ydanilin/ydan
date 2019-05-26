#!/usr/bin/env python

# These two lines are only needed if you don't put the script directly into
# the installation directory
import sys
# sys.path.append('/usr/share/inkscape/extensions')

import inkex


def makeClassString(existing, name):
    class_set = set(filter(lambda x: x, existing.split(" ")))
    class_set.add(name)
    return " ".join(class_set)


def assign_class(name):
    def for_map(element):
        existing = element.get('class', '')
        element.set('class', makeClassString(existing, name))

    return for_map


class HelloWorldEffect(inkex.Effect):
    """
    Example Inkscape effect extension.
    Creates a new layer with a "Hello World!" text centered in the middle of the document.
    """
    def __init__(self):
        inkex.Effect.__init__(self)

        self.OptionParser.add_option(
            '-c', '--classname', action='store',
            type='string', dest='classname', default='',
            help='Class name(s) to assign?')

    def effect(self):
        """
        Effect behaviour.
        Overrides base class' method and inserts "Hello World" text into SVG document.
        """
        if not self.selected:
            sys.stderr.write("Nothing is selected.")
            return
        selection = [v for k, v in self.selected.items()]
        classname_to_add = self.options.classname
        list(map(assign_class(classname_to_add), selection))
        # inkex.debug(selection[0].get('class'))


# Create effect instance and apply it.
effect = HelloWorldEffect()
effect.affect()
