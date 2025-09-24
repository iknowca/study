package org.zerock.w1.calc;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet(name = "calcController", value = "/calc/makeResult")
public class CalcController extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        System.out.println("CalcController..doPost...");
        String num1 = req.getParameter("num1");
        String num2 = req.getParameter("num2");
        System.out.println("num1 : " + num1);
        System.out.println("num2 : " + num2);
        resp.sendRedirect("/index");
    }
}
