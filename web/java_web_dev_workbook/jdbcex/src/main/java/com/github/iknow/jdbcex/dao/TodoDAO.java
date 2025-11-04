package com.github.iknow.jdbcex.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class TodoDAO {

    public String getTime() throws SQLException {
        String now = null;
        try(
                Connection conn = ConnectionUtil.INSTANCE.getConnection();
                PreparedStatement preparedStatement = conn.prepareStatement("select now()");
                ResultSet resultSet = preparedStatement.executeQuery();
        ) {
            resultSet.next();
            now = resultSet.getString(1);
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return now;
    }
}
