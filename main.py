from pyscript import document

# Jan Cabading
# Reused SW1 CODE

#list of current members
g7 = {'Lamelo Ball'}
g8 = {'Lebron James'}
g9 = {'Miku Martineau'}
g10 = {'Jan Cabading', 'Jacob Minguillo'}


def get_member(e):
    # get values from input fields
    f_name = document.getElementById("FIRSTNAME").value  # get the first name
    l_name = document.getElementById("SURNAME").value  # get the last name

    # combine names with a space using concatenation
    fullname = f_name + " " + l_name  # e.g Evaluates to "Miku Martineau" (str)

    new_member = {fullname}

    members = g7 | g8| g9 | g10
    full_list = new_member | members
    members_list = "<br>".join(full_list)
    total_count = len(full_list)

    # format using f-string
    result = f"""
    <h3>Club Roster</h3> 
    <h4>Total Members: {total_count}</h4>
    {members_list}  
    """

    # Display result in HTML element
    document.getElementById("result").innerHTML = result