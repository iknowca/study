package com.iknowca.study.web.jwdw.w2.dao;

import com.iknowca.study.web.jwdw.w2.domain.MemberVO;
import lombok.Cleanup;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class MemberDAO {
    public MemberVO getWithPassword(String mid, String mpw) throws SQLException {
        String query = "SELECT mid, mpw, mname from tbl_member where mid = ? and mpw = ?";

        @Cleanup Connection conn = ConnectionUtil.INSTANCE.getConnection();
        @Cleanup PreparedStatement preparedStatement = conn.prepareStatement(query);
        preparedStatement.setString(1, mid);
        preparedStatement.setString(2, mpw);
        @Cleanup ResultSet resultSet = preparedStatement.executeQuery();
        resultSet.next();
        return MemberVO.builder()
                .mid(resultSet.getString("mid"))
                .mpw(resultSet.getString("mpw"))
                .mname(resultSet.getString("mname"))
                .build();
    }

    public void updateUuid(String mid, String uuid) throws SQLException {
        String sql = "update tbl_member set uuid = ? where mid = ?";
        @Cleanup Connection conn = ConnectionUtil.INSTANCE.getConnection();
        @Cleanup PreparedStatement preparedStatement = conn.prepareStatement(sql);
        preparedStatement.setString(2, mid);
        preparedStatement.setString(1, uuid);
        preparedStatement.executeUpdate();
    }

    public MemberVO selectUUID(String uuid) throws SQLException {
        String sql = "SELECT mid, mpw, mname from tbl_member where uuid = ?";
        @Cleanup Connection conn = ConnectionUtil.INSTANCE.getConnection();
        @Cleanup PreparedStatement preparedStatement = conn.prepareStatement(sql);
        preparedStatement.setString(1, uuid);
        @Cleanup ResultSet resultSet = preparedStatement.executeQuery();
        resultSet.next();
        return MemberVO.builder()
                .mid(resultSet.getString("mid"))
                .mpw(resultSet.getString("mpw"))
                .mname(resultSet.getString("mname"))
                .uuid(resultSet.getString("uuid"))
                .build();
    }
}
