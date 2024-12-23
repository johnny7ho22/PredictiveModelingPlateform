from django.utils.safestring import mark_safe
import copy

"""
自定義的分頁模型
"""
class Pagination(object):

    def __init__(self, request, queryset, page_size = 10, page_param = "page", plus = 5):
        
        #取得get請求網址中問號以後的數據 ex. name=政賢&password=123
        query_dict = copy.deepcopy(request.GET)
        query_dict.mutable = True
           
        self.query_dict = query_dict
        
        #取得當前頁面
        page = request.GET.get(page_param, "1")

        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        #當前頁面
        self.page = page
        
        #取得get的哪一個資料
        self.page_param = page_param
        
        #一頁要顯示多少資料數
        self.page_size = page_size

        #當前頁的起始資料
        self.start = (page - 1) * page_size
        
        #當前頁的最後一筆資料
        self.end = page * page_size

        #要顯示在分頁上的資料
        self.page_queryset = queryset[self.start : self.end]

        #總資料量
        total_count = queryset.count()

        #總頁數
        total_page_count, div = divmod(total_count, page_size)
        
        #在當前頁碼之前要顯示多少頁，在當前頁碼之後要顯示多少頁
        self.plus = plus

        if div:
            total_page_count += 1

        #分頁的總數
        self.total_page_count = total_page_count

    
    #顯示頁碼於前端
    def html(self):
        #計算當前頁碼的前五頁和後五頁
        #如果數據的總頁數小於等於11
        if self.total_page_count <= 11:
            start_page = 1
            end_page = self.total_page_count
        else:
            if self.page <= 5:
                start_page = 1
                end_page = 2 * 5
            else:
                if (self.page + 5) > self.total_page_count:
                    start_page = self.total_page_count - 2 * 5
                    end_page = self.total_page_count
                else:
                    start_page = self.page - 5
                    end_page = self.page + 5

        #顯示頁碼於前端
        page_str_list = []
        
        self.query_dict.setlist(self.page_param, [1])
        
        #首頁
        page_str_list.append(f'<li><a href = "?{self.query_dict.urlencode()}">首頁</a></li>')

        #上一頁
        if self.page == 1:
            self.query_dict.setlist(self.page_param, [1])
            prev = f'<li><a href = "?{self.query_dict.urlencode()}">上一頁</a></li>'
        else:
            self.query_dict.setlist(self.page_param, [self.page-1])
            prev = f'<li><a href = "?{self.query_dict.urlencode()}">上一頁</a></li>'

        page_str_list.append(prev)


        #頁面
        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])

            if i == self.page:
                ele = f'<li class = "active"><a href = "?{self.query_dict.urlencode()}">{i}</a></li>'
            else:
                ele = f'<li><a href = "?{self.query_dict.urlencode()}">{i}</a></li>'

            page_str_list.append(ele)

        #下一頁
        if self.page == self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            next = f'<li><a href = "?{self.query_dict.urlencode()}">下一頁</a></li>'
        else:
            self.query_dict.setlist(self.page_param, [self.page+1])
            next = f'<li><a href = "?{self.query_dict.urlencode()}">下一頁</a></li>'

        page_str_list.append(next)

        #尾頁
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append(f'<li><a href = "?{self.query_dict.urlencode()}">尾頁</a></li>')

        #跳轉頁面
        jump_string = """
        <li>
            <form style="float: left; margin-left: -1px" method="get">
                <div class="input-group" style="width: 200px">
                    <input type="text" name="page" style="position: relative;  display: inline-block; width: 80px;" class="form-control" placeholder="頁碼">
                    <button class="btn btn-default" type="submit">跳轉</button>
                </div>
            </form>
        </li>
        """

        page_str_list.append(jump_string)
            
        page_string = mark_safe("".join(page_str_list))
        
        return page_string



