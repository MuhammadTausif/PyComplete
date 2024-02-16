

feedback = """
                The delivery was fast, and the packaging was excellent. 
                Excellent service overall. Will recommend!
            """
keyword = "excellent"
            
print(f"The word '{keyword}' appears {feedback.count(keyword)} times in the feedback.")


text = """
        Fear leads to anger; anger leads to hate;
        hate leads to suffering.
        This is a path to the dark side.
       """
word = "leads"

print(f"The word '{word}' appears {text.count(word)} times.")

code_snippet = """
                import numpy as np
                np.old_function()
                # Some more code
                np.old_function()
                np.new_function()
               """
deprecated_function = "np.old_function()"
print( f"""The deprecated function appears 
      {code_snippet.count(deprecated_function)}
        times.""")

