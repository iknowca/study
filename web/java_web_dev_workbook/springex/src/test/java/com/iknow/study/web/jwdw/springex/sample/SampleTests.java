package com.iknow.study.web.jwdw.springex.sample;

import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit.jupiter.SpringExtension;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.SQLException;

@Log4j2
@ExtendWith(SpringExtension.class)
@ContextConfiguration(locations = {"classpath:/root-context.xml"})
@RequiredArgsConstructor
public class SampleTests {
    @Autowired
    SampleService sampleService;
    @Autowired
    private DataSource dataSource;

    @Test
    public void testService1() {
        log.info(sampleService);
        Assertions.assertNotNull(sampleService);
    }

    @Test
    public void testConnection() throws SQLException {
        Connection conn = dataSource.getConnection();
        log.info(conn);
        Assertions.assertNotNull(conn);
        conn.close();
    }
}
