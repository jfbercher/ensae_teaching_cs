# -*- coding: utf-8 -*-
"""
@file
@brief Quelques problèmes récurrents avec `IPython <http://ipython.org/>`_.

"""

def notebook_path():
    """
    change matplotlib style

    @param      style       style

    @FAQ(ipython___Récupérer le fichier du notebook depuis le notebook)

    Voir `How to I get the current IPython Notebook name <http://stackoverflow.com/questions/12544056/how-to-i-get-the-current-ipython-notebook-name>`_

    Il suffit d'insérer la cellule suivante dans le notebook ::

        %%javascript
        var kernel = IPython.notebook.kernel;
        var body = document.body,
            attribs = body.attributes;
        var command = "theNotebook = os.path.join(" + "r'"+attribs['data-project'].value+"'," + "r'"+attribs['data-notebook-path'].value+"'," + "r'"+attribs['data-notebook-name'].value+"')";
        kernel.execute(command);

    On peut vérifier que cela fonctionne ::

        theNotebook

    @endFAQ
    """
    pass

def fix_table_notebook():
    """
    @FAQ(ipython___Table des matières à position fixe dans un notebook)
    Il est possible d'ajouter au notebook un menu fix, positionné sur la droite, qui ne bouge pas
    et qui permet de passer d'une section à l'autre plus facilement.

    Voir `Example of a notebook with a fixed index <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/notebooks/exemple_of_fix_menu.html>`_.

    Exemple :

    @code
    <div style="position:absolute; top:10px; right:5px; width:100px; height:90px; margin:10px;">
    [Section 1](#section1) -- [Section 2](#section2) -- [This is the end](#end)
    </div>
    @endcode

    Cette solution peut probablement être améliorée. Elle passe mal lors de la conversion
    du notebook en HTML.

    @endFAQ
    """
    pass

def r_and_notebook():
    """
    @example(techniques___Utiliser R depuis un notebook)

    .. index:: R

    C'est l'objet des deux notebooks :ref:`td2acenoncesession2brst` et la :ref:`correction <td2acorrectionsession2brst>`.

    @endexample

    @FAQ(ipython___Comment utiliser R depuis un notebook ?)

    Voir notebooks :ref:`td2acenoncesession2brst`, :ref:`correction <td2acorrectionsession2brst>`.

    @endFAQ

    """
    pass

def ipython_convert_notebooks():
    """
    @example(techniques___Convertir le notebook en cours au format HTML)

    .. index:: conversion,html,rst

    C'est l'objet du notebook :ref:`notebookconvertrst`.

    @endexample

    @FAQ(ipython___Comment convertir le notebook en cours au format HTML ?)

    Voir notebook :ref:`notebookconvertrst`.

    @endFAQ

    @FAQ(ipython___Comment ajouter un lien vers un fichier local pour le télécharger ?)

    Voir notebook :ref:`notebookconvertrst`.

    @endFAQ

    """
    pass
    
def ipython_get_variable(name, magic_command_instance):
    """
    Retreive the value of a local variable in a notebook.
    
    @param      name                        variable name
    @param      magic_command_instance      instance of `Magics <http://ipython.org/ipython-doc/2/api/generated/IPython.core.magic.html#IPython.core.magic.Magics>`_, 
                                            see `Defining your own magics <http://ipython.org/ipython-doc/2/interactive/reference.html#defining-your-own-magics>`_
    @return                                 value 
    
    The function raises an exception if the context does not exists
    or if the variable name does not value
    
    @FAQ(ipython___Accéder ou modifier une variable du notebook depuis une commande magique)
    
    Lorsqu'on écrit un notebook, toutes les variables qu'on crée sont 
    en quelque sorte globales puisqu'on peut y accéder depuis chaque cellule
    mais leur périmètre est limité au notebook.
    Lorsqu'on crée un commande magique, il est possible d'accéder à ce contexte local
    via le membre ``self.shell.user_ns``. De cette façon, on peut accéder au contenu d'une
    variable, le modifier ou en ajouter une.
    
    @code
    
    class CustomMagics(Magics):
    
        @line_magic
        def custom_cmd(self, line):
            context = self.shell.user_ns
            #...
    
    @endcode
    
    @endFAQ
    """
    if magic_command_instance.shell is None:
        raise Exception("no context, you probably execute this function outside a notebook")
    if name not in magic_command_instance.shell.user_ns:
        raise KeyError("variable {0} not found".format(name))
    return magic_command_instance.shell.user_ns[name]
    