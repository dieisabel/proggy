__all__ = ['blogs']


from django.shortcuts import render


def blogs(request):
    blogs = [
        {
            "title": "Navigating Namespaces and Scope in Python",
            "text": "In a program of any complexity, you’ll create hundreds or thousands of names, each pointing to a specific object. How does Python keep track of all these names so that they don’t interfere with one another? This course covers Python namespaces, the structures used to organize the symbolic names assigned to objects in a Python program.",
            "rating": 4,
            "link": "some post link",
        },
        {
            "title": "Functional Programming in Python: When and How to Use It",
            "text": "Functional programming is a programming paradigm in which the primary method of computation is evaluation of functions. In this tutorial, you’ll explore functional programming in Python.Functional programming typically plays a fairly small role in Python code. But it’s good to be familiar with it. At a minimum, you’ll probably encounter it from time to time when reading code written by others. You may even find situations where it’s advantageous to use Python’s functional programming capabilities in your own code.",
            "rating": 9,
            "link": "post link",
        },
        {
            "title": "Creating PyQt Layouts for GUI Applications",
            "text": "PyQt’s layout managers provide a user-friendly and productive way of arranging graphical components, or widgets, on a GUI. Laying out widgets properly will make your GUI applications look polished and professional. Learning to do so efficiently and effectively is a fundamental skill for you to get up and running with GUI application development using Python and PyQt.",
            "rating": 10,
            "link": "another post link",
        },
        {
            "title": "Pandas Sort: Your Guide to Sorting Data in Python",
            "text": "Learning pandas sort methods is a great way to start with or practice doing basic data analysis using Python. Most commonly, data analysis is done with spreadsheets, SQL, or pandas. One of the great things about using pandas is that it can handle a large amount of data and offers highly performant data manipulation capabilities.In this tutorial, you’ll learn how to use .sort_values() and .sort_index(), which will enable you to sort data efficiently in a DataFrame.",
            "rating": 2,
            "link": "pandas link",
        },
        {
            "title": "Python Inner Functions: What Are They Good For?",
            "text": "Inner functions, also known as nested functions, are functions that you define inside other functions. In Python, this kind of function has direct access to variables and names defined in the enclosing function. Inner functions have many uses, most notably as closure factories and decorator functions.",
            "rating": 7,
            "link": "inner link",
        },
        {
            "title": "Stochastic Gradient Descent Algorithm With Python and NumPy",
            "text": "Stochastic gradient descent is an optimization algorithm often used in machine learning applications to find the model parameters that correspond to the best fit between predicted and actual outputs. It’s an inexact but powerful technique.Stochastic gradient descent is widely used in machine learning applications. Combined with backpropagation, it’s dominant in neural network training applications",
            "rating": 5,
            "link": "some numpy",
        },
    ]
    context = {
        "blogs": blogs,
    }
    return render(request, 'blog/blogs.html', context)
