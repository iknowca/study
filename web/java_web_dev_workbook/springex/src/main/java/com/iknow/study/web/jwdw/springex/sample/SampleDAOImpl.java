package com.iknow.study.web.jwdw.springex.sample;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Repository;

@Repository
@Qualifier("sampleDAOImpl")
public class SampleDAOImpl implements SampleDAO {

}
