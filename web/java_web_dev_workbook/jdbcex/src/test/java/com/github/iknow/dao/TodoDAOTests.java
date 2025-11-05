package com.github.iknow.dao;

import com.github.iknow.jdbcex.dao.TodoDAO;
import com.github.iknow.jdbcex.domain.TodoVO;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.sql.SQLException;
import java.time.LocalDate;
import java.util.List;

public class TodoDAOTests {
    private TodoDAO todoDAO;

    @BeforeEach
    public void ready() {
        todoDAO = new TodoDAO();
    }

    @Test
    public void testTime() throws SQLException {
        System.out.println(todoDAO.getTime());
    }

    @Test
    public void testInsert() throws SQLException {
        TodoVO vo = TodoVO.builder()
                .title("test")
                .dueDate(LocalDate.of(2025, 11, 5))
                .build();
        todoDAO.insert(vo);
    }

    @Test
    public void testList() throws SQLException {
        List<TodoVO> list = todoDAO.selectAll();
        list.forEach(System.out::println);
    }

    @Test
    public void testSelectOne() throws SQLException {
        TodoVO vo = todoDAO.selectOne(1L);
        System.out.println(vo);
    }

    @Test
    public void testUpdate() throws SQLException {
        TodoVO vo = TodoVO.builder()
                .tno(1L)
                .title("test")
                .dueDate(LocalDate.of(2025, 11, 5))
                .build();
        todoDAO.updateOne(vo);
    }
}
