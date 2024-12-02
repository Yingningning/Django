class Pagenation(object):
    def __init__(self,request,queryset,page_size=10,plus=5,page_param="page"):
        page = request.GET.get(page_param,'1')
        if not page.isdigit():
            page = 1
        else:
            page = int(page)
        self.plus = plus
        self.page = page
        self.page_size = page_size
        
        self.start = page*page_size-page_size
        self.end = page*page_size
        
        sum_page = queryset.count()//self.page_size +1
        self.start_page = self.page-plus if self.page >plus else 1
        self.end_page = self.start_page + page_size if self.start_page + page_size < sum_page else sum_page
        
        self.page_queryset = queryset[self.start:self.end]
        
    def html(self):
        page_str_list = []
        for i in range(self.start_page,self.end_page+1):
            if i == self.page:
                ele = '<li class="page-item active"><a class="page-link" href="?page={}">{}</a></li>'.format(i,i)
            else:
                ele = '<li class="page-item"><a class="page-link" href="?page={}">{}</a></li>'.format(i,i)
            page_str_list.append(ele)
        page_str = "".join(page_str_list)
        return page_str