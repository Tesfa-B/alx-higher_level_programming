class MyList(list):
    """
    A subclass of list that provides addtional
    """
    def print_sorted(self):
        """
        prints sorted in ascending order
        """
        sorted_li = sorted(self)
        print(sorted_li)
