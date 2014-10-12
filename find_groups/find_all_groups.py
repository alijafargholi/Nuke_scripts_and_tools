"""
A simple function that will help you to find all the Groups Node inside
your nuke script. You could simply store the return value into a variable
and loop through it to do something with them

.. module:: `find_all_groups`
   :platform: Unix, Windows
   :synopsis: query all the groups nodes.

.. moduleauthor:: Chad Dombrova
"""

def find_all_groups(group_level=nuke.root()):
    """
    This def will scan the given group to find and store the other existing
    groups. This function will recursively be executed til all the groups
    inside the nuke script is founded. Finally it will yield them

    :param group_level: address of the group level to scan
    :yield: generator of group nodes
    """
    with group_level:
        # Scan all the nodes in current group level to find a "Group" node
        for group in (i for i in nuke.allNodes() if i.Class() == "Group"):
            # Once a "Group" node is found, add it to the list
            yield group
            # Recursively scan inside the newly founded group to
            # find more groups.
            for subgroup in find_all_groups(group):
                yield subgroup
