package com.iknowca.study.web.jwdw.w2.controller;

import com.iknowca.study.web.jwdw.w2.dto.TodoDTO;
import com.iknowca.study.web.jwdw.w2.service.TodoService;
import jakarta.servlet.ServletContext;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.extern.log4j.Log4j2;

import java.util.List;

@WebServlet(name="todoListController", value="/todo/list")
@Log4j2
public class TodoListController extends HttpServlet {
    private final TodoService todoService = TodoService.INSTANCE;

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException {
        log.info("doGet /todo/list");

        ServletContext context = req.getServletContext();
        log.info("appName: " + context.getAttribute("appName"));

        try {
            List<TodoDTO> dtoList = todoService.listAll();
            req.setAttribute("dtoList", dtoList);
            req.getRequestDispatcher("/WEB-INF/todo/list.jsp").forward(req, resp);
        } catch (Exception e) {
            log.error(e.getMessage(), e);
            throw new ServletException("list error");
        }
    }
}
