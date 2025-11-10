package com.iknowca.study.web.jwdw.w2.service;

import com.iknowca.study.web.jwdw.w2.dto.TodoDTO;
import lombok.extern.log4j.Log4j2;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.sql.SQLException;
import java.time.LocalDate;

@Log4j2
public class TodoServiceTest {
    private TodoService service;

    @BeforeEach
    public void ready() {
        service = TodoService.INSTANCE;
    }

    @Test
    public void testRegister() throws SQLException {
        TodoDTO todoDTO = TodoDTO.builder()
                .title("JDBC Test Title")
                .dueDate(LocalDate.now())
                .build();
        log.info("--------------------------------------");
        log.info(todoDTO);
        service.register(todoDTO);
    }
}
