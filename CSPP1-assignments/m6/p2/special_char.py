'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
        Read string from the input, store it in variable str_input.
        '''
    str_input = input()
    output_str = ""
    for str_iterator in str_input:
        if str_iterator in "!@#$%^&*":
            output_str += " "
        else:
            output_str += str_iterator
    print(output_str)

if __name__ == "__main__":
    main()
