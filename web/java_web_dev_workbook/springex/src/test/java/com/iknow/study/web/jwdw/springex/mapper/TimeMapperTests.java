package com.iknow.study.web.jwdw.springex.mapper;

import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit.jupiter.SpringExtension;

@Log4j2
@ExtendWith(SpringExtension.class)
@ContextConfiguration(locations = {"classpath:/root-context.xml"})
@RequiredArgsConstructor
public class TimeMapperTests {

    @Autowired(required = false)
    private TimeMapper timeMapper;
    @Autowired(required = false)
    private TimeMapper2 timeMapper2;

    @Test
    public void testGetTime() {
        log.info(timeMapper.getTime());
    }

    @Test
    public void testGetTime2(){
        log.info(timeMapper2.getNow());
    }

}
