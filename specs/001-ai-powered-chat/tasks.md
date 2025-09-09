# Tasks: AI-Powered Financial Dashboard with Chat Assistant

**Input**: Design documents from `/specs/001-ai-powered-chat/`
**Prerequisites**: plan.md, research.md, data-model.md (all complete)

## Path Structure (Web Application)
- **Backend**: `backend/src/`, `backend/tests/`
- **Frontend**: `frontend/src/`, `frontend/tests/`
- **Shared**: Root level configuration and documentation

## Phase 3.1: Setup & Project Structure

- [x] T001 Create project directory structure (backend/, frontend/, docs/)
- [x] T002 Initialize backend Python project with FastAPI dependencies (requirements.txt)
- [x] T003 Initialize frontend Python project with Streamlit dependencies (requirements.txt)
- [x] T004 [P] Configure backend linting (black, flake8, mypy) in backend/pyproject.toml
- [x] T005 [P] Configure frontend linting (black, flake8) in frontend/pyproject.toml
- [x] T006 [P] Setup environment configuration (.env.example, config.py)
- [x] T007 [P] Initialize git hooks for pre-commit (black, tests)

## Phase 3.2: API Contracts & Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3

**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**

### Contract Tests (API Endpoints)
- [ ] T008 [P] Contract test GET /api/companies/search in backend/tests/contract/test_companies_search.py
- [ ] T009 [P] Contract test GET /api/companies/{ticker}/data in backend/tests/contract/test_financial_data.py
- [ ] T010 [P] Contract test GET /api/companies/{ticker}/comparables in backend/tests/contract/test_comparables.py
- [ ] T011 [P] Contract test POST /api/chat/query in backend/tests/contract/test_chat_api.py
- [ ] T012 [P] Contract test GET /api/charts/{ticker}/valuation in backend/tests/contract/test_charts_api.py

### Integration Tests (User Workflows)
- [ ] T013 [P] Integration test company search workflow in backend/tests/integration/test_company_search_flow.py
- [ ] T014 [P] Integration test financial data retrieval in backend/tests/integration/test_data_pipeline.py
- [ ] T015 [P] Integration test AI chat with context in backend/tests/integration/test_ai_assistant.py
- [ ] T016 [P] Integration test chart data generation in backend/tests/integration/test_chart_generation.py

## Phase 3.3: Data Models (ONLY after tests are failing)

- [ ] T017 [P] Company model in backend/src/models/company.py
- [ ] T018 [P] FinancialData model in backend/src/models/financial_data.py
- [ ] T019 [P] ComparableCompanies model in backend/src/models/comparable_companies.py
- [ ] T020 [P] AnalystCoverage model in backend/src/models/analyst_coverage.py
- [ ] T021 [P] SentimentData model in backend/src/models/sentiment_data.py
- [ ] T022 [P] UserSession model in backend/src/models/user_session.py
- [ ] T023 [P] ChartConfiguration model in backend/src/models/chart_configuration.py

## Phase 3.4: Core Services

### Financial Data Services
- [ ] T024 [P] FinancialDataService (yfinance integration) in backend/src/services/financial_data_service.py
- [ ] T025 [P] CompanySearchService (company lookup) in backend/src/services/company_search_service.py
- [ ] T026 [P] ComparablesService (peer analysis) in backend/src/services/comparables_service.py
- [ ] T027 [P] SentimentService (news/social sentiment) in backend/src/services/sentiment_service.py

### AI & Chat Services
- [ ] T028 AIAssistantService (LangChain + Azure OpenAI) in backend/src/services/ai_assistant_service.py
- [ ] T029 ConversationService (chat history management) in backend/src/services/conversation_service.py

### Chart & Visualization Services
- [ ] T030 [P] ChartDataService (Plotly data preparation) in backend/src/services/chart_data_service.py
- [ ] T031 [P] SessionService (user state management) in backend/src/services/session_service.py

## Phase 3.5: CLI Commands (Library Testing)

- [ ] T032 [P] CLI financial-data --search AAPL --format json in backend/src/cli/financial_data_cli.py
- [ ] T033 [P] CLI ai-assistant --query "compare PE ratios" --context data.json in backend/src/cli/ai_assistant_cli.py
- [ ] T034 [P] CLI chart-viz --type valuation --companies AAPL,MSFT in backend/src/cli/chart_viz_cli.py

## Phase 3.6: API Endpoints Implementation

- [ ] T035 GET /api/companies/search endpoint in backend/src/api/companies.py
- [ ] T036 GET /api/companies/{ticker}/data endpoint in backend/src/api/companies.py
- [ ] T037 GET /api/companies/{ticker}/comparables endpoint in backend/src/api/companies.py
- [ ] T038 POST /api/chat/query endpoint in backend/src/api/chat.py
- [ ] T039 GET /api/charts/{ticker}/valuation endpoint in backend/src/api/charts.py
- [ ] T040 GET /api/charts/{ticker}/trading endpoint in backend/src/api/charts.py
- [ ] T041 GET /api/charts/{ticker}/sentiment endpoint in backend/src/api/charts.py

## Phase 3.7: Frontend Components

### Streamlit Components
- [x] T042 [P] SearchWidget component in frontend/src/components/search_widget.py
- [x] T043 [P] ChartDisplay component in frontend/src/components/chart_display.py
- [x] T044 [P] ChatInterface component in frontend/src/components/chat_interface.py
- [x] T045 [P] DashboardLayout component in frontend/src/components/dashboard_layout.py

### Pages
- [x] T046 Main dashboard page in frontend/src/pages/dashboard.py
- [ ] T047 Company analysis page in frontend/src/pages/company_analysis.py
- [ ] T048 [P] Settings page in frontend/src/pages/settings.py

### Frontend Services
- [x] T049 [P] APIClient for backend communication in frontend/src/services/api_client.py
- [x] T050 [P] SessionManager for frontend state in frontend/src/services/session_manager.py

## Phase 3.8: Integration & Middleware

- [ ] T051 Database connection setup (SQLite) in backend/src/database/connection.py
- [ ] T052 Caching layer (Redis integration) in backend/src/cache/redis_client.py
- [ ] T053 Error handling middleware in backend/src/middleware/error_handler.py
- [ ] T054 Logging configuration in backend/src/utils/logging_config.py
- [ ] T055 CORS and security headers in backend/src/middleware/security.py

## Phase 3.9: Frontend-Backend Integration Tests

- [ ] T056 [P] Frontend search widget → backend API test in frontend/tests/integration/test_search_integration.py
- [ ] T057 [P] Chat interface → AI backend test in frontend/tests/integration/test_chat_integration.py
- [ ] T058 [P] Chart display → chart API test in frontend/tests/integration/test_chart_integration.py

## Phase 3.10: Performance & Polish

### Unit Tests
- [ ] T059 [P] Unit tests for financial data validation in backend/tests/unit/test_financial_data_validation.py
- [ ] T060 [P] Unit tests for AI prompt engineering in backend/tests/unit/test_ai_prompts.py
- [ ] T061 [P] Unit tests for chart data formatting in backend/tests/unit/test_chart_formatting.py

### Performance & Documentation
- [ ] T062 Performance tests (API response times <3s) in backend/tests/performance/test_api_performance.py
- [ ] T063 [P] Update API documentation (OpenAPI spec) in docs/api-spec.yaml
- [ ] T064 [P] Create deployment guide in docs/deployment.md
- [ ] T065 [P] Create user guide with screenshots in docs/user-guide.md

### Final Validation
- [ ] T066 Run complete end-to-end workflow test
- [ ] T067 Validate Azure OpenAI cost optimization
- [ ] T068 Performance validation (chart rendering <2s)
- [ ] T069 Remove code duplication and cleanup
- [ ] T070 Manual testing checklist execution

## Dependencies

### Phase Dependencies
- Setup (T001-T007) → Tests (T008-T016) → Models (T017-T023) → Services (T024-T031) → Implementation (T032-T041)

### Key Blocking Dependencies
- T017-T023 (Models) before T024-T031 (Services)
- T024-T031 (Services) before T035-T041 (API Endpoints) 
- T035-T041 (API) before T042-T050 (Frontend Components)
- T051-T055 (Infrastructure) before T056-T058 (Integration Tests)

### Parallel Execution Groups
```bash
# Phase 3.2 - All contract tests can run in parallel
T008, T009, T010, T011, T012  # Contract tests
T013, T014, T015, T016        # Integration tests

# Phase 3.3 - All models are independent
T017, T018, T019, T020, T021, T022, T023

# Phase 3.4 - Services with no dependencies
T024, T025, T026, T027, T030, T031

# Phase 3.7 - Independent frontend components
T042, T043, T044, T045, T048, T049, T050
```

## Validation Checklist

- [x] All API endpoints have contract tests (T008-T012)
- [x] All data models have creation tasks (T017-T023)
- [x] All tests come before implementation (Phase 3.2 before 3.3+)
- [x] Parallel tasks are truly independent (different files)
- [x] Each task specifies exact file path
- [x] TDD cycle enforced (tests must fail first)

## Success Criteria

1. **Functional**: All 15 functional requirements from spec.md implemented
2. **Performance**: Chart rendering <2s, AI responses <3s
3. **Quality**: 90%+ test coverage, all tests passing
4. **Architecture**: Libraries expose CLI, proper separation of concerns
5. **Cost**: Azure OpenAI usage <$15/month for expected load 