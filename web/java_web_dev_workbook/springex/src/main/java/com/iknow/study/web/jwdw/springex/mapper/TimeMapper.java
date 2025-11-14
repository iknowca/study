package com.iknow.study.web.jwdw.springex.mapper;

import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

public interface TimeMapper {
    @Select("select now()")
    String getTime();
}
