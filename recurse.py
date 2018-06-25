#! /usr/local/bin/python3

# Write a function that returns "inclusion" if the given projection specification represents an
# inclusion projection and "exclusion" if the given projection specification represents an exclusion
# projection. Throw an error if the projection specification is invalid.
#
# get_projection_kind({"a.b": "include", "d": "include"}) ==> "inclusion"
# get_projection_kind({"a": {"b": "exclude", "c": "exclude"}}) ==> "exclusion"
# get_projection_kind({"a.b": "include", "d": "exclude"}) ==> invalid
# get_projection_kind({"a" : {}}) ==> "inclusion"

def projection_validation(projecton_val):
    """
    Descriptiion -
        This method returns the type of projection value validation

    Mandatory Args -
        projecton_val (str) - Projection value to be validated

    Return -
        Projection Type (str)
    """
    if projecton_val in ["exclude", "include"]:
        return_val = projecton_val
    elif projecton_val is []:
        return_val = "include"
    else:
        return_val = "Unknown"

    return return_val

def get_projection_type(dict_var):
    """
    Descriptiion -
        This is a method which recursively finds what are the values in the given dictionary.

    Mandatory Args -
        dict_var (dict) - Dictionary for which you wish to find projection

    Return -
        Projection Type (str)
    """
    projection_list = []

    for value in dict_var.values():
        if isinstance(value, dict):
            projection_list.append(get_projection_type(value))
        else:
            projection_list.append(projection_validation(value))
    if projection_list == [] or len(list(set(projection_list))) == 0:
        return "include"
    elif len(list(set(projection_list))) != 1:
        return "invalid"
    else:
        return projection_list.pop()

if __name__ == "__main__":
    # List of scenarios
    my_dict_list = [{"a": {"b": "exclude", "c": "exclude"}}, {"a.b": "include", "d": "include"}, {"a.b": "include", "d": "exclude"}, {"a": {"b": "exclude", "c": {"d": "exclude", "e": "exclude"}}}, {"a" : {}}, {}, {"a": {"b": "exclude", "c": {"d": "exclude", "e": "include"}}}]

    # Iterate through dictionary to find all projection
    for each_dict in my_dict_list:
        print("")
        print("Dict       : {}".format(each_dict))
        print("Projection : {}".format(get_projection_type(each_dict)))
        print("")
