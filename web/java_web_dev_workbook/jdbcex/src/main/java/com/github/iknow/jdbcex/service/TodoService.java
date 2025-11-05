package com.github.iknow.jdbcex.service;

import com.github.iknow.jdbcex.dao.TodoDAO;
import com.github.iknow.jdbcex.domain.TodoVO;
import com.github.iknow.jdbcex.dto.TodoDTO;
import com.github.iknow.jdbcex.util.MapperUtil;
import lombok.extern.log4j.Log4j2;
import org.modelmapper.ModelMapper;

import java.sql.SQLException;
import java.util.List;
import java.util.stream.Collectors;

@Log4j2
public enum TodoService {
    INSTANCE;

    private TodoDAO dao;
    private ModelMapper modelMapper;

    TodoService() {
        dao = new TodoDAO();
        modelMapper = MapperUtil.INSTANCE.get();
    }

    public List<TodoDTO> listAll() throws SQLException {
        List<TodoVO> voList = dao.selectAll();
        log.info("voList....................");
        log.info(voList);

        return voList.stream()
                .map(vo -> modelMapper.map(vo, TodoDTO.class))
                .collect(Collectors.toList());
    }

    public void register(TodoDTO todoDTO) throws SQLException {
        TodoVO vo = modelMapper.map(todoDTO, TodoVO.class);
        log.info(vo);

        dao.insert(vo);
    }

    public TodoDTO get(Long tno) throws SQLException {
        log.info("tno: " + tno);
        TodoVO vo = dao.selectOne(tno);
        return modelMapper.map(vo, TodoDTO.class);
    }

    public void remove(Long tno) throws SQLException {
        log.info("tno: " + tno);
        dao.deleteOne(tno);
    }

    public void modify(TodoDTO todoDTO) throws SQLException {
        log.info("todoDTO: " + todoDTO);
        TodoVO vo = modelMapper.map(todoDTO, TodoVO.class);
        dao.updateOne(vo);
    }
}
