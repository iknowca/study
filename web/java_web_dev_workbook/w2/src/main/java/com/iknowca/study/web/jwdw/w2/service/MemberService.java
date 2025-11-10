package com.iknowca.study.web.jwdw.w2.service;

import com.iknowca.study.web.jwdw.w2.dao.MemberDAO;
import com.iknowca.study.web.jwdw.w2.domain.MemberVO;
import com.iknowca.study.web.jwdw.w2.dto.MemberDTO;
import lombok.extern.log4j.Log4j2;
import org.eclipse.tags.shaded.org.apache.bcel.generic.INSTANCEOF;
import org.modelmapper.ModelMapper;

import java.sql.SQLException;

@Log4j2
public enum MemberService {
    INSTANCE;

    private MemberDAO dao;
    private ModelMapper modelMapper;

    MemberService() {
        dao = new MemberDAO();
        modelMapper = new ModelMapper();
    }

    public MemberDTO login(String mid, String mpw) throws SQLException {
        MemberVO vo = dao.getWithPassword(mid, mpw);
        return modelMapper.map(vo, MemberDTO.class);
    }

    public void updateUuid(String mid, String uuid) throws SQLException {
        dao.updateUuid(mid, uuid);
    }

    public MemberDTO getByUUID(String uuid) throws SQLException {
        MemberVO vo = dao.selectUUID(uuid);
        return modelMapper.map(vo, MemberDTO.class);
    }
}
