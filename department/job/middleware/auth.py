from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,redirect

class AuthMiddleware(MiddlewareMixin):
    
    def process_request(self,request):
        
        # 0.排除不需要登录的页面
        # request.path_info 获取当前请求的路径。
        if request.path_info in ['/login','/img_code']:
            return
        
        # 如果没有返回值(即返回None),继续执行下一个中间件的process_request方法
        # 如果返回值不为None,则终止执行,直接返回该值作为响应
        
        # 1. 读取session中的用户信息，如果用户信息存在，则继续执行，否则跳转到登录页面
        info_dict = request.session.get('info')
        if info_dict:
            return
        return redirect('/login')
        
    # def process_response(self,request,response):
    #     # print("M1: process_response")
    #     return response