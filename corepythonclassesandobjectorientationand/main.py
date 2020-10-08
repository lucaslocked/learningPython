# What I'll Learn
    # Defining Per-Class
    # Using Properties
    # Represent Objects As Strings
    # Method Resolution
    # Transforming Classes With Object-Decorators
    # Creating Simple Data Classes
    # How To Create Idiomatic Python Classes

# Prerequisites
    # Python Essentials
        # Functions, Classes, and Modules
    # Everything From Core Python: Getting Started & Core Python: Functions & Functional Programming


# Class Attributes, Methods, And Properties
    # Overview
        # Review
            # Class Definition
            # Initializer Definition
            # Instance Attributes
        # Class Attributes
        # Static Methods
        # Class Methods
        # Interactions With Inheritance
        # Properties
        # Specializing Properties
        # Designing For Extensibility

    # Terminology
        # Naming Special Functions
            # __specialfunction__
            # Dunder
                # A Portmanteau Of "Double Underscore"
                # Instead Of Saying "Underscore Underscore Name Underscore Underscore", Just Say "Dunder Name"
        # Instance Attributes
            # Assigned On A Per Object Basis, Usually Used By The Dunder Init Method Of A Class

            # Instance Attributes

    # Choosing Between @staticmethod And @classmethod
        # @classmethod
            # Requires Access To The Class Object To Call Other Class Methods To The Constructor
        # @staticmethod
            # No Access Needed To Either Class Or Instance Objects
            # Most Likely An Implementation Detail Of The Class
            # May Be Able To Be Moved Outside The Class To Become A Global Scope Function In The Module

    # The 'Named Constructor' Idiom
        # A Factory Method Which Returns An Instance Of A Class. The Method Name Allows Callers To Express Intent, And Allows Construction To Be Performed With Different Combinations Of Arguements.
        # It Was Originally A C++ Idiom, But It Is Also Applicable To Python