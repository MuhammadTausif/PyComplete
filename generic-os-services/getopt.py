import sys
import getopt

def main(argv):
    # Initialize variables to store command line arguments
    input_file = ''
    output_file = ''

    # Define the command line argument format
    short_options = "hi:o:"
    long_options = ["help", "input=", "output="]

    # Try to parse the command line arguments
    try:
        # Parse the arguments
        opts, args = getopt.getopt(argv, short_options, long_options)
    except Exception: # getopt.GetoptError:
        # Print the usage message if the arguments are not valid
        print('Usage: test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    # Iterate over the options and arguments
    for opt, arg in opts:
        if opt == '-h':
            # Print the help message
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--input"):
            # Set the input file
            input_file = arg
        elif opt in ("-o", "--output"):
            # Set the output file
            output_file = arg

    # Print the input and output file names
    print('Input file is "', input_file)
    print('Output file is "', output_file)

# Call the main function with the command line arguments minus the script name
if __name__ == "__main__":
    main(sys.argv[1:])
